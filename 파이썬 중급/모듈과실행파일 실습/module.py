import unitConversion as uc

if __name__ == '__main__':
    inputNumber = int(input('길이(cm)을 입력하세요 : '))

    returnMm = uc.cmToMm(inputNumber)
    returnInch = uc.cmToInch(inputNumber)
    returnM = uc.cmToM(inputNumber)
    returnFt = uc.cmToFt(inputNumber)

    print(f'10cm : {returnMm}mm')
    print(f'10cm : {returnInch}inch')
    print(f'10cm : {returnM}m')
    print(f'10cm : {returnFt}ft')