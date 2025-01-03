from math import ceil
# Ввод данных с консоли
try:
    Q = float(input("Введите суточную выработку готовой продукции (т): "))
    if Q < 0:
        raise ValueError("Суточная выработка не может быть отрицательной.")

    t = float(input("Введите продолжительность рабочей смены (ч): "))
    if t <= 0:
        raise ValueError("Продолжительность смены должна быть больше нуля.")

    M = float(input("Введите производительность одного пельменного автомата (т/ч): "))
    if M <= 0:
        raise ValueError("Производительность автомата должна быть больше нуля.")

    # Расчет производительности линии
    P = Q / (2 * t)
    print(f"Производительность линии изготовления пельменей: {P:.2f} т/ч")

    # Расчет необходимого количества автоматов
    n = P / M
    print(f"Необходимое количество пельменных автоматов: {ceil(n)} (округлено вверх)")

    # Ввод данных для подготовки теста
    a = float(input("Введите массовую долю теста в готовой продукции (%): "))
    if not (0 < a <= 100):
        raise ValueError("Массовая доля теста должна быть в диапазоне от 0 до 100.")

    mixerM = float(input("Введите производительность тестомесильной машины (т/ч): "))
    if mixerM <= 0:
        raise ValueError("Производительность тестомесильной машины должна быть больше нуля.")

    # Расчет производительности линии подготовки теста
    L = (a * P) / 100
    print(f"Производительность линии подготовки теста: {L:.2f} т/ч")

    # Расчет необходимого количества тестомесильных машин
    doughMixerCount = L / mixerM
    print(f"Необходимое количество тестомесильных машин: {ceil(doughMixerCount)} (округлено вверх)")

    # Ввод данных для подготовки фарша
    meatPercentage = float(input("Введите массовую долю мяса в готовой продукции (%): "))
    eggPercentage = float(input("Введите массовую долю яиц в готовой продукции (%): "))
    saltPercentage = float(input("Введите массовую долю соли в готовой продукции (%): "))
    spicesPercentage = float(input("Введите массовую долю специй в готовой продукции (%): "))

    if not (0 <= meatPercentage + eggPercentage + saltPercentage + spicesPercentage <= 100):
        raise ValueError("Суммарная массовая доля компонентов фарша должна быть в диапазоне от 0 до 100.")

    cutterPerformance = float(input("Введите производительность куттера (т/ч): "))
    if cutterPerformance <= 0:
        raise ValueError("Производительность куттера должна быть больше нуля.")

    # Расчет производительности линии подготовки фарша
    mincedMeat = ((meatPercentage + eggPercentage + saltPercentage + spicesPercentage) * P) / 100
    print(f"Производительность линии подготовки фарша: {mincedMeat:.2f} т/ч")

    # Расчет необходимого количества куттеров
    cutterCount = mincedMeat / cutterPerformance
    print(f"Необходимое количество куттеров: {ceil(cutterCount)} (округлено вверх)")

except ValueError as e:
    print(f"Ошибка ввода: {e}")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")