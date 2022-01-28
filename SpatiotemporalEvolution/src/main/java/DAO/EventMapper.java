package DAO;

import Entity.Event;
import org.apache.ibatis.annotations.Param;

import java.util.Date;
import java.util.List;

public interface EventMapper {
    //新建一个事件
    int save(Event accidentEvent);
    //根据ID删除一个事件
    int delete(int id);
    //根据ID查找一个事件
    Event findByID(int id);
    //查找所有事件
    List<Event> findAll();
    //查找某个武器出现的事件数
    int findCountByNum(String weaponName);
    //查找某个武器出现的事件数
    int findCountByNumDate(@Param("weaponName")String weaponName,@Param("startTime") String start, @Param("endTime") String end);
    //查找某个地点出现的事件数
    int LocCountByNumDate(@Param("LocName")String LocName,@Param("startTime") String start, @Param("endTime") String end);
    //查找所有事件
    int getCount(@Param("startTime") String start,@Param("endTime") String end);
    //查找所有事件
    List<Event> getALL(@Param("startTime") String start,@Param("endTime") String end);
}
