CREATE OR REPLACE PACKAGE orm_message IS


    TYPE orm_message IS RECORD(
        orm_user orm_message.textmes%TYPE,
        users_count INTEGER
    );


    TYPE tbls IS TABLE OF mess_data;

    FUNCTION GetMesData (text_mes orm_message.txtmes%TYPE default null)
        RETURN tblmesdata
        PIPELINED;

END orm_message;




CREATE OR REPLACE PACKAGE BODY orm_message IS

    FUNCTION GetMesData (text_mes orm_message.text_mes%TYPE default null)
    RETURN tblsmesdata
    PIPELINED
    IS

        TYPE mes IS REF mes_user;
        mes_user  mes;

        mes_data mes_data;
        query_str varchar2(1000);

    begin

        query_str :='select orm_message.text_mes, count(orm_message.time_send)
                        from orm_message ';

        -- optional part where
            if text_mes is not null then
             query_str:= query_str||' where trim(orm_message.text_mes) = trim('''||text_mes||''') ''';
            end if;
        -- end optional part

        query_str := query_str||' group by (orm_message.time_send';



        OPEN orm_message FOR query_str;
        LOOP
            FETCH text_mes into text_data;
            exit when (text_mes %NOTFOUND);

            PIPE ROW (text_data);

        END LOOP;


    END GetSkillData;

END orm_message;
