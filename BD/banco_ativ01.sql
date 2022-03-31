create table medico(
    id text primary key not null,
    nome text not null,
    cidade text not null,
    cpf integer not null,
    rg integer not null,
    especialidade text not null,
    unique(rg,cpf)
);

create table paciente(
    id text primary key not null,
    nome text not null,
    cidade text not null,
    cpf integer not null,
    rg integer not null,
    doenca text not null,
    unique(rg,cpf)
);

create table consulta(
    medico_id integer not null,
    paciente_id integer not null,
    horario integer not null,
    primary key (medico_id,paciente_id,horario),
    foreign key (medico_id) references medico(id),
    foreign key (paciente_id) references paciente(id));