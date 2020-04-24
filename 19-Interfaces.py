class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        Resultado = 0
        x = 1
        while x <= n:
            if n % x == 0:
                Resultado += x
            x += 1
        return Resultado
