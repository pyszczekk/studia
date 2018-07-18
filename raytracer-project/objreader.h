#ifndef _OBJREADER_H
#define _OBJREADER_H
#define ILOSC 100000
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <math.h>
#include <stdlib.h> 
#include "vec.h"
#include "ray.h"
#include "bmp.h"
#include "light.h"
#include "triangle.h"
using namespace std;
class ObjReader{
private:
Vector *v;
Triangle *t;
long long size;

public:
ObjReader(){};
ObjReader(const ObjReader& r){v=r.v; t =r.t; size=r.size;};
~ObjReader(){/*
    if(v!=NULL) delete [] v; if(t!=NULL)delete []t;*/}
void ReadVectors(const string& nazwa, double _x,double _y,double z, double _s, unsigned char r=255, unsigned char g=255, unsigned char b=255){
	ifstream plik;
 	string linia;
 	char x;
 	string line;
 	string word;
 	v=new Vector[ILOSC];
 	t=new Triangle[ILOSC];
 	int j=0;
 	int n=0;
    plik.open(nazwa);
	bool normal=false;
	bool texture=false;
    
        _s=_s+(z/100);

    if (_s<=0)_s=0.1;
    if(plik.good() == true && j<ILOSC && n<ILOSC)
    {	
    	
    	double tab[3];
        while(plik>>word)
        {
        	if (word=="v"){
        		int i=0;
        		while(i<3){
        			plik>>word;
        			std::string::size_type sz;
        			tab[i]=stod (word, &sz);
        			
        			i++;
        		}
        		v[j].set_values(_x+_s*tab[0], _y-_s*tab[1],_s*tab[2]+z);
        		j++;
        	}
        	if(word=="f"){
        		int k=0;
        		while(k<3){
        			plik>>word;
        			std::string::size_type sz;
        			tab[k]=stod(word,&sz);
                    //cout<<tab[k]<<" "
        			k++;
        		}
        		
        		t[n].set_values(this->getV(tab[0]-1),this->getV(tab[1]-1),this->getV(tab[2]-1));
                t[n].set_color(r,g,b);
        		n++;
        	}
        	
       } 
    }else{
    	size=0;
    	std::cout<<"nie moge otworzyc pliku"<<std::endl;
    }
    plik.close();
    size=n;
	}
	Vector& getV(long x){
		return v[x]; 
	}
	Triangle& getT(long x){
		return t[x];
	}
	long long getSize(){
		return size;
	}

};
#endif