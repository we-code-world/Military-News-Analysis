package Service;

import DAO.AdministratorMapper;
import DAO.UserMapper;
import Entity.Administrator;
import Entity.User;
import com.github.pagehelper.PageInfo;

public interface UserInfoService {

    void setUserMapper(UserMapper userMapper);

    void setAdministratorMapper(AdministratorMapper administratorMapper);

    //创建一个新用户
    int setUser(User user);

    //查找用户
    User findByAccount(String account);

    //查找管理员
    Administrator findByAccountAdmin(String account);

    //分页查找所有用户
    PageInfo<User> pageAll(int pageNum, int pageSize);
}
