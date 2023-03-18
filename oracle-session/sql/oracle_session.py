def query():
    return """
SELECT *
FROM (SELECT sess.sid,
             sess.serial#,
             sess.wait_time,
             sess.seconds_in_wait,
             sess.state,
             sess.event,
             sess.username,
             sess.osuser,
             sess.machine,
             sess.program,
             sess.type,
             sess.sql_child_number,
             sess.sql_exec_start,
             sess.sql_id,
             (SELECT sql.sql_fulltext
              FROM v$sql sql
              WHERE sess.sql_id = sql.sql_id
                  FETCH FIRST 1 ROWS ONLY) sql_fulltext,
             sess.prev_exec_start,
             sess.prev_sql_id,
             (SELECT sql.sql_fulltext
              FROM v$sql sql
              WHERE sess.prev_sql_id = sql.sql_id
                  FETCH FIRST 1 ROWS ONLY) prev_sql_fulltext,
             blocking_session
      FROM v$session sess
      WHERE sess.username != 'SYS'
      ORDER BY logon_time DESC)
WHERE sql_fulltext IS NOT NULL
"""
