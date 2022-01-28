package DAO;

import Entity.Location;

import java.util.List;

public interface LocationMapper {
    //新建一个地点
    int save(Location loc);
    //根据ID删除一个地点
    int delete(int id);
    //根据level和ConName查找标准地点
    List<Location> findByCountryAndLevel(String ConName,int level);
    //根据level和ConName查找标准地点
    Location findByID(int posID);
    //查找所有地点
    List<Location> findAll();
}
