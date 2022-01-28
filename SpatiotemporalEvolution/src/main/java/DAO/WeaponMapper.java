package DAO;

import Entity.Weapon;

import java.util.List;

public interface WeaponMapper {
    //新建一个事件
    int save(Weapon weapon);
    //根据ID删除一个事件
    int delete(int weaponID);
    //查找全部武器
    Weapon findByID(int weaponID);
    //查找全部武器
    List<Weapon> findAll();
    //查找武器ID
    List<Weapon> findAllBySClass(String SClass);
    //查找武器ID
    List<Weapon> findAllByWeapon(String Weapon);
    //查找所有大类别
    List<String> findAllClass();
    //查找所有小类别
    List<String> findAllSClass(String Class);
    //查找所有武器
    List<String> findAllweapons(String SClass);
}
