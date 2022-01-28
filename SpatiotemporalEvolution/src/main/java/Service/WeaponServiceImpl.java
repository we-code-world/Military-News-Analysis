package Service;

import DAO.KeySentenceMapper;
import DAO.WeaponMapper;
import Entity.KeySentence;
import Entity.Weapon;
import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;
import net.sf.json.JSONArray;
import net.sf.json.JSONObject;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class WeaponServiceImpl implements WeaponService{
    private WeaponMapper weaponMapper;
    private KeySentenceMapper keySentenceMapper;

    public void setWeaponMapper(WeaponMapper weaponMapper) {
        this.weaponMapper = weaponMapper;
    }

    public void setKeySentenceMapper(KeySentenceMapper keySentenceMapper) {
        this.keySentenceMapper = keySentenceMapper;
    }

    @Override
    public List<String> getAllWeapons(String SClass) {
        List<String> list = weaponMapper.findAllweapons(SClass);
        return list;
    }

    @Override
    public List<String> getAllSClass(String Class) {
        List<String> list = weaponMapper.findAllSClass(Class);
        return list;
    }

    @Override
    public List<String> getAllClass() {
        List<String> list = weaponMapper.findAllClass();
        return list;
    }

    @Override
    public List<Weapon> getAll() {
        List<Weapon> list = weaponMapper.findAll();
        return list;
    }

    @Override
    public JSONObject getClassAndSClassInEvent(JSONArray weaponIDs) {
        JSONObject res_map = new JSONObject();
        for (String Class:getAllClass()) {
            res_map.put(Class,0);
            for (String SClass:getAllSClass(Class)){
                res_map.put(SClass,0);
            }
        }
        JSONObject jsonObject;
        Weapon weapon;
        String this_class,this_sclass;
        int number,id;
        for (int i=0;i<weaponIDs.size();i++){
            jsonObject = (JSONObject) weaponIDs.get(i);
            id = Integer.parseInt((String) jsonObject.get("ID"));
            weapon = weaponMapper.findByID(id);
            this_class = weapon.getWeaponClass();
            this_sclass = weapon.getWeaponSClass();
            if (this_class.equals("") || this_sclass.equals(""))continue;
            number = (int)jsonObject.get("NUMBER");
            res_map.put(this_sclass,(int)res_map.get(this_sclass)+number);
            res_map.put(this_class,(int)res_map.get(this_class)+number);
        }
        return res_map;
    }

    @Override
    public PageInfo<Weapon> pageAllWeapons(int pageNum, int pageSize) {
        PageHelper.startPage(pageNum,pageSize);
        List<Weapon> list = weaponMapper.findAll();
        PageInfo<Weapon> page = new PageInfo<Weapon>(list);
        return page;
    }

    @Override
    public KeySentence getSentenceByID(int sentenceID) {
        return keySentenceMapper.findByID(sentenceID);
    }

    @Override
    public List<KeySentence> getAllKeySentencesByNewsID(int NewsID) {
        List<KeySentence> list = keySentenceMapper.findAllByNewsID(NewsID);
        return list;
    }

    @Override
    public KeySentence getAllKeySentencesByNewsIDAndNum(int NewsID,int num) {
        return keySentenceMapper.findAllByNewsIDAndNum(NewsID,num);
    }

    @Override
    public PageInfo<KeySentence> pageAllKeySentences(int pageNum, int pageSize) {
        PageHelper.startPage(pageNum,pageSize);
        List<KeySentence> list = keySentenceMapper.findAll();
        PageInfo<KeySentence> page = new PageInfo<KeySentence>(list);
        return page;
    }

    @Override
    public JSONObject getClassObj() {
        JSONObject classObj = new JSONObject();
        List<String> Classes = getAllClass();
        for (String Class:Classes) {
            classObj.put(Class,getAllSClass(Class));
        }
        return classObj;
    }

    @Override
    public List<Weapon> getAllWeaponsByName(String Name) {
        return weaponMapper.findAllByWeapon(Name);
    }

    @Override
    public List<Weapon> getAllWeaponsBySClass(String SClass) {
        return weaponMapper.findAllBySClass(SClass);
    }
}
