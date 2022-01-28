package DAO;

import Entity.Administrator;

import java.util.List;

public interface AdministratorMapper {
    //新建一个管理员
    int save(Administrator admin);
    //根据ID删除一个管理员
    int delete(int id);
    //通过账号查找管理员
    Administrator findByAccount(String Account);
    //通过ID查找管理员
    Administrator findByID(int id);
    //查找所有管理员
    List<Administrator> findAll();
}
