package Service;

import DAO.AdministratorMapper;
import DAO.UserMapper;
import Entity.Administrator;
import Entity.User;
import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;

import java.util.List;

public class UserInfoServiceImpl implements UserInfoService{
    private UserMapper userMapper;
    private AdministratorMapper administratorMapper;
    @Override
    public void setUserMapper(UserMapper userMapper) {
        this.userMapper = userMapper;
    }

    @Override
    public void setAdministratorMapper(AdministratorMapper administratorMapper) {
        this.administratorMapper = administratorMapper;
    }

    //创建一个新用户
    @Override
    public int setUser(User user) {
        return userMapper.save(user);
    }

    //查找用户
    @Override
    public User findByAccount(String account) {
        return userMapper.findByAccount(account);
    }
    //查找用户
    @Override
    public Administrator findByAccountAdmin(String account) {
        return administratorMapper.findByAccount(account);
    }
    //分页实现查找所有的求购信息
    public PageInfo<User> pageAll(int pageNum, int pageSize){
        PageHelper.startPage(pageNum,pageSize);
        List<User> list = userMapper.findAll();
        PageInfo<User> page = new PageInfo<User>(list);
        return page;
    }
}
