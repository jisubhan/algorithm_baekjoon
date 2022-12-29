SELECT MCDP_CD AS "진료과코드" , COUNT(*) AS "5월예약건수" 
FROM APPOINTMENT
GROUP BY MCDP_CD , TO_CHAR(APNT_YMD , 'MM') 
HAVING TO_CHAR(APNT_YMD , 'MM') IN ('05')
ORDER BY COUNT(*) ASC , MCDP_CD ASC