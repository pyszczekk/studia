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
#include "trace.h"
int main(){
	const uint16_t imgWidth2 = 500;
	const uint16_t imgHeight2 = 500;
	JiMP2::BMP bmp2(imgWidth2, imgHeight2);
	bmp2.setBackground();
	Triangle triangle(Vector(250,30,0),Vector(100,420,50),Vector(270,420,0),255,0,0);
	Triangle triangle2(Vector(100,190,40),Vector(360,120,0),Vector(20,20,0),0,255,0);
	Triangle triangle3(Vector(430,190,10),Vector(300,450,10),Vector(420,420,0),0,0,255);
	unsigned char color2[3]={255,255,255};
	Light light(Vector(250,250,100),0.75,color2[0],color2[1],color2[2]);
	Obj *obj[3];
	obj[0]=&triangle;
	obj[1]=&triangle2;
	obj[2]=&triangle3;

	for(uint16_t y=0; y<imgHeight2; y++){
		for(uint16_t x=0; x<imgWidth2; x++){
			Ray ray(Vector(x,y,0), Vector(0,0,1));
			double t = 100000;
			Obj *hitObject = NULL;
			//for(uint16_t i=0; i<3;++i){
				if(trace(ray,obj,t,hitObject,3)){
				Vector pc = ray.getOrigin() + ray.getDirection()*t;

				Vector L = Normalize(light.getPos() -pc);
				Vector N = Normalize(hitObject->getNormal(pc));

				double dt = L.scalar(N);
				double r,g,b;
				r=hitObject->getR()+ light.getR()*dt*light.getIntensity();
				g=hitObject->getG()+ light.getG()*dt*light.getIntensity();
				b=hitObject->getB()+light.getB()*dt*light.getIntensity();
				if(r<0)r=0;
				if(g<0)g=0;
				if(b<0)b=0;
				if(r>255)r=255;
				if(g>255)g=255;
				if(b>255)b=255;
				bmp2.setPixel(x,y, (int)r,(int)g,(int)b);
			//}
		}
			/*
			if(triangle.cross(ray,t)){
				//crossing point
				Vector pc = ray.getOrigin() + ray.getDirection()*t;
				Vector L = Normalize(light2.getPos() -pc);
				Vector N = Normalize(triangle.getNormal());
				double dt = L.scalar(N);
				double r,g,b;
				r=0+ light2.getR()*dt*light2.getIntensity();
				g=255+ light2.getG()*dt*light2.getIntensity();
				b=0+light2.getB()*dt*light2.getIntensity();
				if(r<0)r=0;
				if(g<0)g=0;
				if(b<0)b=0;
				if(r>255)r=255;
				if(g>255)g=255;
				if(b>255)b=255;
				bmp2.setPixel(x,y, (int)r,(int)g,(int)b);
			}
			if(triangle2.cross(ray,t)){
				//crossing point
				Vector pc = ray.getOrigin() + ray.getDirection()*t;
				Vector L = Normalize(light2.getPos() -pc);
				Vector N = Normalize(triangle2.getNormal());
				double dt = L.scalar(N);
				double r,g,b;
				r=255+ light2.getR()*dt*light2.getIntensity();
				g=100+ light2.getG()*dt*light2.getIntensity();
				b=80+light2.getB()*dt*light2.getIntensity();
				if(r<0)r=0;
				if(g<0)g=0;
				if(b<0)b=0;
				if(r>255)r=255;
				if(g>255)g=255;
				if(b>255)b=255;
				bmp2.setPixel(x,y, (int)r,(int)g,(int)b);
			}
			if(triangle3.cross(ray,t)){
				//crossing point
				Vector pc = ray.getOrigin() + ray.getDirection()*t;
				Vector L = Normalize(light2.getPos() -pc);
				Vector N = Normalize(triangle3.getNormal());
				double dt = L.scalar(N);
				double r,g,b;
				r=80+ light2.getR()*dt*light2.getIntensity();
				g=100+ light2.getG()*dt*light2.getIntensity();
				b=255+light2.getB()*dt*light2.getIntensity();
				if(r<0)r=0;
				if(g<0)g=0;
				if(b<0)b=0;
				if(r>255)r=255;
				if(g>255)g=255;
				if(b>255)b=255;
				bmp2.setPixel(x,y, (int)r,(int)g,(int)b);
			}
			*/
		}
	}
	
	std::ofstream outfile("main2.bmp", std::ofstream::binary);
	outfile << bmp2;

	std::cout << "end." << std::endl;
return 0;

}