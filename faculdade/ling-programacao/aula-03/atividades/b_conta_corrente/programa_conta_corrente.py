from conta_corrente import ContaPF, ContaPJ

conta_pf1 = ContaPF('João das Couves', '111.111.111.11')
conta_pf1.depositar(1000)

print(f'Saldo atual é: R$ {conta_pf1.saldo}')
print(f'Receberá empréstimo = {conta_pf1.solicitar_emprestimo(2000)}')

conta_pf1.sacar(800)

print('Saldo atual é', conta_pf1.saldo)
print('Receberá empréstimo = ', conta_pf1.solicitar_emprestimo(2000))

conta_pj1 = ContaPJ("Empresa A", "11.111.111/1111-11")
print(f'\nSaldo atual é: R$ {conta_pj1.saldo}')
print('Receberá empréstimo = ', conta_pj1.sacar_emprestimo(3000))
