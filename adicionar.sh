#!/bin/bash
echo "Adicionando arquivos..."
if ! git add $1
then 
	echo "Erro ao adicionar atualizar"
	exit 1
fi
git commit -am "Exerc�cio Resolvido"
git pull
faelsfernandes
Fernandes5672
echo "Adicionado com sucesso!"

exit 1