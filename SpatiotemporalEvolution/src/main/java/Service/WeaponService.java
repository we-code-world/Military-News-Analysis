package Service;

import DAO.WeaponMapper;
import DAO.KeySentenceMapper;
import Entity.KeySentence;
import Entity.Weapon;
import com.github.pagehelper.PageInfo;
import net.sf.json.JSONArray;
import net.sf.json.JSONObject;

import java.util.List;

public interface WeaponService {
    void setWeaponMapper(WeaponMapper weaponMapper);

    void setKeySentenceMapper(KeySentenceMapper keySentenceMapper);

    //查找所有武器名
    List<String> getAllWeapons(String SClass);

    //查找所有小类别
    List<String> getAllSClass(String Class);

    //查找所有大类别
    List<String> getAllClass();

    //查找全部武器
    List<Weapon> getAll();

    //查找所有事件中出现的大类别和小类别
    JSONObject getClassAndSClassInEvent(JSONArray weaponIDs);

    //分页查找所有武器
    PageInfo<Weapon> pageAllWeapons(int pageNum, int pageSize);

    //通过关键句编号查找关键句
    KeySentence getSentenceByID(int sentenceID);

    //通过新闻编号查找所有关键句
    List<KeySentence> getAllKeySentencesByNewsID(int NewsID);

    //通过新闻编号和关键句在新闻中的序号查找所有关键句
    KeySentence getAllKeySentencesByNewsIDAndNum(int NewsID,int num);

    //分页查找所有关键句
    PageInfo<KeySentence> pageAllKeySentences(int pageNum, int pageSize);

    JSONObject getClassObj();

    List<Weapon> getAllWeaponsByName(String Name);

    List<Weapon> getAllWeaponsBySClass(String SClass);
}
