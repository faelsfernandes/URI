#!/bin/bash
echo "Adicionando arquivos..."
if ! git add $1
then 
	echo "Erro au atualizar"
	exit 1
fi
git commit -am "Exercício Resolvido"
echo "Adicionado com sucesso!"

exit 1