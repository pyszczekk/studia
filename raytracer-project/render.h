#ifndef _RENDER_H
#define _RENDER_H
#include <iostream>
#include <fstream>
#include <cstring>
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
void render(vector<Obj*>& obj, vector <Light>& lights,JiMP2::BMP& bmp, uint16_t imgWidth, uint16_t imgHeight, double camX, double camY, double camZ){
		for(uint16_t y=0; y<imgHeight; y++){
		for(uint16_t x=0; x<imgWidth; x++){
			Ray ray(Vector(x+camX,y+camZ,0+camZ), Vector(0,0,1));
			double t = 1000000;
			long long i=0;
			Obj *hitObject = NULL;
			//for(uint16_t i=0; i<4;++i){
				//cout<<trace(ray,obj,t,hitObject)<<endl;
				if(trace(ray,obj,t,hitObject,obj.size())){
				Vector pc = ray.getOrigin() + ray.getDirection()*t;

				vector<Vector> L;
				Vector N = Normalize(hitObject->getNormal(pc));

				vector <double> dt;
				double r,g,b;
				for(vector<Light>::iterator it=lights.begin();it!=lights.end();++it){
					L.push_back(Normalize(it->getPos() -pc));
					dt.push_back((Normalize(it->getPos() -pc)).scalar(N));
				}
				double ref = 0.4;
				long long asd=0;
				double red=0;
				double green=0;
				double blue=0;
				if(hitObject->Phong()){
					for(int i=0; i<lights.size();++i){
						Vector rr = 2*dt.at(i)*N -L.at(i);
						double spec = pow(rr.scalar(ray.getDirection()),4);
						red+=lights.at(i).getR()*dt.at(i)*lights.at(i).getIntensity()*(1-ref)+lights.at(i).getR()*lights.at(i).getIntensity()*dt.at(i)*spec;
						blue+=lights.at(i).getB()*dt.at(i)*lights.at(i).getIntensity()*(1-ref)+lights.at(i).getB()*lights.at(i).getIntensity()*dt.at(i)*spec;
						green+=lights.at(i).getG()*dt.at(i)*lights.at(i).getIntensity()*(1-ref)+lights.at(i).getG()*lights.at(i).getIntensity()*dt.at(i)*spec;
					} 
				}else{
					for(int i=0; i<lights.size();++i){
						red+=lights.at(i).getR()*dt.at(i)*lights.at(i).getIntensity()*(1-ref);
						blue+=lights.at(i).getB()*dt.at(i)*lights.at(i).getIntensity()*(1-ref);
						green+=lights.at(i).getG()*dt.at(i)*lights.at(i).getIntensity()*(1-ref);
					} 
				}
				r=ref*hitObject->getR()+ red;
				g=ref*hitObject->getG()+ green;
				b=ref*hitObject->getB()+ blue;
				if(r<0)r=0;
				if(g<0)g=0;
				if(b<0)b=0;
				if(r>255)r=255;
				if(g>255)g=255;
				if(b>255)b=255;
				bmp.setPixel(x,y, (int)r,(int)g,(int)b);
			}
		}
	}
	
}

#endif