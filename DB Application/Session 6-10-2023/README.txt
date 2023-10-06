insert all 
into netflix values ('101','Star','Web show','19/10/2021','comedy','director',6,6,255,'4.5',499,'Yes','english','Italy')
into netflix values ('102','Star Wars','Action Movies','19/10/2021','Fiction','aaa',6,6,255,'3.6',499,'Yes','english','Italy')
into netflix values ('103','Peakly Blinder','(90s films','19/10/2021','Action','aaa',6,6,255,'3.0',499,'Yes','english','Italy')
into netflix values ('104','Just a select','something','19/10/2021','Comedy','aaa',6,6,255,'3.1',499,'Yes','english','Italy')
into netflix values ('105','ZNMD','Web show','19/10/2021','Action','aaa',6,6,255,'3.9',499,'Yes','english','Italy')
select * from dual;


insert all 
into netflix values ('106','Mirzapur','Web show','19/10/2021','Comedy','karan p',6,6,260,'3.4',499,'No','Hindi','India')
into netflix values ('107','Family Man','Web show','19/10/2021','Fiction','xyz',6,6,280,'3.4',499,'No','Hindi','India')
select * from dual;





DELETE
FROM
    netflix
WHERE
    contentid='101';


commit;  // save data server
