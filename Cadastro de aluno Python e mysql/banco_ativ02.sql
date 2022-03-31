create table aluno(
    numero integer primary key not null,
    nome text not null,
    curso text not null,
    nota1 real not null,
    nota2 real not null,
    nota3 real not null,
    nota4 real not null,
    situacao text not null,
    unique(numero)
);

--drop table aluno;

