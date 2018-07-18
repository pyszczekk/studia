#ifndef _FILEREADER_H
#define _FILEREADER_H
#include <iostream>
#include <fstream>
#include <cstring>
#include<cmath>
#include <sstream>
#include "vec.h"
#include "ray.h"
#include "obj.h"
#include "sphere.h"
#include "bmp.h"
#include "light.h"
#include "triangle.h"
#include "objreader.h"
#include <vector>
#include "trace.h"
#include "render.h"
using namespace std;
void readFile(const string& nazwa, JiMP2::BMP bmp,  uint16_t imgWidth,  uint16_t imgHeight, const string& wyjscie){
	ifstream plik;
	string linia;
  	string word;
 	vector<Obj*> obj;
 	vector <Light> lights;
 	vector <ObjReader> ob;
 	int camX, camY, camZ;
 	camX=0;
 	camY=0;
 	camZ=0;
 	plik.open(nazwa);
 	std::string::size_type sz;

 	if(plik.good()==true){
 		int il=0;
 		//std::cout<<"ok";
 		//getline(plik,linia);
 		while(!plik.eof()){
 			//std::cout<<word;
 			il++;
 			plik>>word;
 			getline(plik,linia);

 			if(word == "OBJ"){ //8 argumentow;
 				double x,y,z, scale;
 				unsigned char r,g,b;
 				string name;
 				//std::cout<<word<<std::endl;
 				int arg=0;
 				for(int i=1; i<linia.length();i++){
			            			string wyr="";
			            			
			            			int j=i;
			            			while(linia[j]!=' '&& j<linia.length()){
			            				wyr+=linia[j];
			            				j++;
			            			}
			            			cout<<wyr<<endl;
			            			arg++;
			            			
			            			switch(arg){
			            				case 1:
			            					name = wyr;
			            					break;
			            				case 2:
			            					x=round(stod(wyr,&sz));
			            					break;
			            				case 3:
			            					y=round(stod(wyr,&sz));
			            					break;
			            				case 4:
			            					z=round(stod(wyr,&sz));
			            					break;
			            				case 5:
			            					r=atoi(wyr.c_str());
			            					break;
			            				case 6:
			            					g=atoi(wyr.c_str());
			            					break;
			            				case 7:
			            					b = atoi(wyr.c_str());
			            					break;
			            				case 8:
			            					scale =stod(wyr,&sz);
			            					break;

			            			};
			            			
			            			i=j;
			            		};
			         if(arg!=8){
			         	std::cout<<"błąd w linijce: "<<il<<std::endl;
			         }else{
			        ObjReader o;
					o.ReadVectors(name, x,y,z,scale, r,g,b);
					ob.push_back(o);
					}
 			}
 			if(word == "LIGHT"){
 				double x,y,z, intense;
 				unsigned char r,g,b;
 				int arg=0;
 				for(int i=1; i<linia.length();i++){
			            			string wyr="";
			            			
			            			int j=i;
			            			while(linia[j]!=' ' && j<linia.length()){
			            				wyr+=linia[j];
			            				j++;
			            			}
			            			cout<<wyr<<endl;
			            			arg++;
			            			switch(arg){
			            		
			            				case 1:
			            					x=round(stod(wyr,&sz));
			            					break;
			            				case 2:
			            					y=round(stod(wyr,&sz));
			            					break;
			            				case 3:
			            					z=round(stod(wyr,&sz));
			            					break;
			            				case 4:
			            					intense=round(stod(wyr,&sz));
			            					break;
			            				case 5:
			            					r=atoi(wyr.c_str());
			            					break;
			            				case 6:
			            					g = atoi(wyr.c_str());
			            					break;
			            				case 7:
			            					b = atoi(wyr.c_str());
			            					break;

			            			};
			            			
			            			i=j;
			            		};
			         if(arg!=7){
			         	std::cout<<"błąd w linijce: "<<il<<std::endl;
			         }else{
				         Light li(Vector(x,y,z),intense,r,g,b);
				      	 lights.push_back(li);
			      	}
 			}
 			if(word == "SPHERE"){
 				double x,y,z, rad;
 				unsigned char r,g,b;
 				bool phong;
 				int arg=0;
 				for(int i=1; i<linia.length();i++){
			            			string wyr="";
			            			
			            			int j=i;
			            			while(linia[j]!=' ' && j<linia.length()){
			            				wyr+=linia[j];
			            				j++;
			            			}
			            			cout<<wyr<<endl;
			            			arg++;
			            			switch(arg){
			            		
			            				case 1:
			            					x=round(stod(wyr,&sz));
			            					break;
			            				case 2:
			            					y=round(stod(wyr,&sz));
			            					break;
			            				case 3:
			            					z=round(stod(wyr,&sz));
			            					break;
			            				case 4:
			            					rad=round(stod(wyr,&sz));
			            					break;
			            				case 5:
			            					r=atoi(wyr.c_str());
			            					break;
			            				case 6:
			            					g = atoi(wyr.c_str());
			            					break;
			            				case 7:
			            					b = atoi(wyr.c_str());
			            					break;
			            				case 8:
			            					if(wyr=="0") phong=false;
			            					else phong=true;
			            					break;

			            			};
			            			
			            			i=j;
			            		};
			         if(arg!=8){
			         	std::cout<<"błąd w linijce: "<<il<<std::endl;
			         }else{
			      	 obj.push_back(new Sphere(Vector(x, y, z), rad, r,g,b,phong));
			      	}
 			}
 			if(word == "TRIANGLE"){
 					double ax,ay,az,bx,by,bz,cx,cy,cz;
 				unsigned char r,g,b;
 				
 				int arg=0;
 				for(int i=1; i<linia.length();i++){
			            			string wyr="";
			            			
			            			int j=i;
			            			while(linia[j]!=' ' && j<linia.length()){
			            				wyr+=linia[j];
			            				j++;
			            			}
			            			cout<<wyr<<endl;
			            			arg++;
			            			switch(arg){
			            		
			            				case 1:
			            					ax=round(stod(wyr,&sz));
			            					break;
			            				case 2:
			            					ay=round(stod(wyr,&sz));
			            					break;
			            				case 3:
			            					az=round(stod(wyr,&sz));
			            					break;
			            				case 4:
			            					bx=round(stod(wyr,&sz));
			            					break;
			            				case 5:
			            					by=round(stod(wyr,&sz));
			            					break;
			            				case 6:
			            					bz=round(stod(wyr,&sz));
			            					break;
			            				case 7:
			            					cx=round(stod(wyr,&sz));
			            					break;
			            				case 8:
			            					cy=round(stod(wyr,&sz));
			            					break;
			            				case 9:
			            					cz=round(stod(wyr,&sz));
			            					break;
			            				case 10:
			            					r=atoi(wyr.c_str());
			            					break;
			            				case 11:
			            					g=atoi(wyr.c_str());
			            					break;
			            				case 12:
			            					b=atoi(wyr.c_str());
			            					break;
			            			};
			            			
			            			i=j;
			            		};
			         if(arg!=12){
			         	std::cout<<"błąd w linijce: "<<il<<std::endl;
			         }else{
			      	 obj.push_back(new Triangle(Vector(ax, ay, az), Vector(bx, by, bz), Vector(cx, cy, cz),r,g,b));
			      	}
 			}
 			if(word == "CAMERA"){
 				double x,y,z, intense;
 				unsigned char r,g,b;
 				int arg=0;
 				for(int i=1; i<linia.length();i++){
			            			string wyr="";
			            			
			            			int j=i;
			            			while(linia[j]!=' ' && j<linia.length()){
			            				wyr+=linia[j];
			            				j++;
			            			}
			            			arg++;
			            			switch(arg){
			            		
			            				case 1:
			            					x=round(stod(wyr,&sz));
			            					break;
			            				case 2:
			            					y=round(stod(wyr,&sz));
			            					break;
			            				case 3:
			            					z=round(stod(wyr,&sz));
			            					break;

			            			};
			            			
			            			i=j;
			            		};
			         if(arg!=3){
			         	std::cout<<"błąd w linijce: "<<il<<std::endl;
			         }else{
				         camX=x;
				         camY=y;
				         camZ=z;
			      	}
 			}
 		}
 		plik.close();
 		render(obj,lights,bmp,imgWidth,imgHeight,camX,camY,camZ);
 		if(ob.size())
 		for(int j=0; j<ob.size();++j){
 			double size=ob.at(j).getSize();
 		for(uint16_t y=0; y<imgHeight; y++){
			for(uint16_t x=0; x<imgWidth; x++){
				//zamienic dir z orig ? 
				double t = 1000000;
				Ray ray(Vector(x+camX,y+camY,0), Vector(0,0,1)); 
				long long i=0;
				//cout<<t<<" t"<<endl;
				while(i<size){

					if(ob.at(j).getT(i).cross(ray,t)){
					Vector pc = ray.getOrigin() + ray.getDirection()*t;

					vector<Vector> L;
					Vector N = Normalize(ob.at(j).getT(i).getNormal());

						vector <double> dt;
						double r,g,b;
						for(vector<Light>::iterator it=lights.begin();it!=lights.end();++it){
							L.push_back(Normalize(it->getPos() -pc));
							dt.push_back((Normalize(it->getPos() -pc)).scalar(N));
						}
					double _r,_g,_b;
					double ref=0.4;
					double red=0;
					double green=0;
					double blue=0;
					for(int k=0; k<lights.size();++k){
						red+=lights.at(k).getR()*dt.at(k)*lights.at(k).getIntensity()*(1-ref);
						blue+=lights.at(k).getB()*dt.at(k)*lights.at(k).getIntensity()*(1-ref);
						green+=lights.at(k).getG()*dt.at(k)*lights.at(k).getIntensity()*(1-ref);
					} 
					_r=ob.at(j).getT(i).getR()*ref+ red;
					_g=ob.at(j).getT(i).getG()*ref+ green;
					_b=ob.at(j).getT(i).getB()*ref+ blue;
					if(_r<0)_r=0;
					if(_g<0)_g=0;
					if(_b<0)_b=0;
					if(_r>255)_r=255;
					if(_g>255)_g=255;
					if(_b>255)_b=255;
					bmp.setPixel(x,y, (int)_r,(int)_g,(int)_b);
					};
					i++;
				}
				cout<<x<<" "<<y<<endl;
			
				
			}
		}
	
 }
ofstream outfile(wyjscie, std::ofstream::binary);
	outfile << bmp;

	cout << "end." << std::endl;
 	}else{
 		cout<<"nie udalo sie odczytac pliku"<<std::endl;
 	}
 	obj.clear();
	lights.clear();

}
#endif