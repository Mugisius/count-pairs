from behave import *
from os import chmod
import subprocess


@given('ничего')
def step_impl(context):
    pass

@given('подготовили тестовый файл "{filename}"')
def step_impl(context, filename):
    context.file = 'texts/'+filename

@given('подготовили закрытый файл "{filename}"')
def step_impl(context, filename):
    context.file = 'texts/'+filename
    chmod('texts/'+filename, 0)


@when('запускаем приложение count_pairs.py с {number:d} аргументом(ами)')
def step_impl(context, number):
    cmd = 'python3 count_pairs.py {context.file} ' + ' '.join(['sun', 'bird', '0'][:number-1])
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    context.result = result

@when('запускаем приложение count_pairs.py с несуществующим файлом')
def step_impl(context):
    cmd = 'python3 count_pairs.py unreal.file sun bird 0'
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    context.result = result

@when('ищем пару слов "{firstW}" и "{secondW}" на расстоянии {dist}')
def step_smpl(context, firstW, secondW, dist):
    cmd = f'python3 count_pairs.py {context.file} {firstW} {secondW} {dist}'
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    context.result = result


@then('получаем сообщение об ошибке с параметрами')
def step_impl(context):
    out = context.result.stderr
    assert out.startswith('usage')

@then('получаем сообщение об ошибке с файлом')
def step_impl(context):
    out = context.result.stderr
    assert out.startswith('Ошибка при работе с файлом')

@then('находим {number} таких пар в тестовом файле')
def step_impl(context, number):
    out = context.result.stdout
    assert out.split()[0] == number
