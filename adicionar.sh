#!/bin/bash
echo "Adicionando arquivos..."
if ! git add $1
then 
	echo "Erro ao adicionar atualizar"
	exit 1
fi
git commit -am "Exercício Resolvido"
git pull
echo "Adicionado com sucesso!"

exit 1