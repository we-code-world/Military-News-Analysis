package Entity;

public class Weapon {
    private int weaponID;
    private String weaponName;
    private String weaponClass;
    private String weaponSClass;
    private String weaponCountry;

    public void setWeaponID(int weaponID){ this.weaponID = weaponID; }
    public int getWeaponID(){ return this.weaponID; }

    public void setWeaponName(String weaponName){ this.weaponName = weaponName; }
    public String getWeaponName(){ return this.weaponName; }

    public void setWeaponClass(String weaponClass){ this.weaponClass = weaponClass; }
    public String getWeaponClass(){ return this.weaponClass; }

    public void setWeaponSClass(String weaponSClass){ this.weaponSClass = weaponSClass; }
    public String getWeaponSClass(){ return this.weaponSClass; }

    public void setWeaponCountry(String weaponCountry){ this.weaponCountry = weaponCountry; }
    public String getWeaponCountry(){ return this.weaponCountry; }
}
