package Entity;

import java.util.ArrayList;
import java.util.List;

public class Section {
    public String name;
    public String category;
    public int id;
    public double start;
    public double end;
    public double point;
    public Section(double Start,double End,String Name,String Category,int ID){
        this.name = Name;
        this.category = Category;
        this.id = ID;
        this.start =Start;
        this.end = End;
        this.point = (Start + end)/2;
    }
    public List<Section> getRootChild(List<String> Names,int startNumber){
        List<Section> sections = new ArrayList<>();
        int number = Names.size();
        double Space = (this.end - this.start)/number;
        for (int i =0; i <number ; i++)
            sections.add(new Section(this.start+i*Space,this.start+i*Space+Space,Names.get(i),Names.get(i),i+startNumber));
        return sections;
    }
    public List<Section> getChild(List<String> Names,int startNumber){
        List<Section> sections = new ArrayList<>();
        int number = Names.size();
        double Space = (this.end - this.start)/number;
        for (int i =0; i <number ; i++)
            sections.add(new Section(this.start+i*Space,this.start+i*Space+Space,Names.get(i),this.category,startNumber+i));
        return sections;
    }
    public List<Link> getLinks(List<String> Names,int startNumber){
        List<Link> links = new ArrayList<>();
        int number = Names.size();
        for (int i =0; i <number ; i++)
            links.add(new Link(this.id,startNumber+i));
        return links;
    }
}
