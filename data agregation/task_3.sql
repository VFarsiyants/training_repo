-- (�� �������) ����������� ������������ ����� � ������� �������.

drop table if exists for_task_3;
create table for_task_3 (value int);

truncate table for_task_3; 
insert into for_task_3(value) values (1),(2),(3),(4),(5);

-- ����� ��������� ������� mysql � �� ����� ������������ ����� �������, ������ ������� ����������� ���������� ����������� ���������� (ln) � ����� ������� (sum), ����� 
-- ��������� ���������� ���������� (exp). ��� ��������� ��� ��������������� ��������� ���������� - �������� ������������ ����� ����� ����������. 
-- ����� �������� ������������ ���������� ��� ��� ������� ��� ���������� � ���������� ������� ��������.
select exp(sum(ln(value))) from for_task_3 ft;