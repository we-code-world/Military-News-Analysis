package Entity;

public class Link {
    public String source;
    public String target;
    public Link(){
        source="";
        target="";
    }
    public Link(String s,String t){
        source=s;
        target=t;
    }
    public Link(int a,int b){
        source="" + a;
        target="" + b;
    }
}
