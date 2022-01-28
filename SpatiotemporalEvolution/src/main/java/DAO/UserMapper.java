package DAO;

import Entity.User;

import java.util.List;

public interface UserMapper {
    //保存一个新的用户
    int save(User user);
    //通过ID删除一个用户
    int delete(int id);
    //更改用户信息
    int change(User user);
    //通过ID查找用户
    User findByID(int id);
    //通过账号查找用户
    User findByAccount(String account);
    //查找所有用户
    List<User> findAll();
}
