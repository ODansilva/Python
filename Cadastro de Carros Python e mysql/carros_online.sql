create table carros(
    valor integer not null,
    ano integer not null,
    modelo text not null,
    marca text not null,
    combustível text not null,
    placa not null,
    renavam integer not null,
    descrição text not null,
    telefone integer not null,
    unique (placa,renavam)
);
select * from carros
drop table carros;
insert into carros (valor, ano, modelo, marca, combustível, placa, renavam, descrição, telefone) values (2500, 2018, 'pablo vittar', 'mitsubisha', 'gaytanol', '6667896', 123456783, 'teu cu', 999998824);