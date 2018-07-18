#include <iostream>
#include <fstream>
#include <cstring>
#include "vec.h"
#include "ray.h"
#include "sphere.h"
#include "bmp.h"
#include "light.h"
#include "triangle.h"
#include "objreader.h"
#include <cmath>
int main(){
	const uint16_t imgWidth3 = 500;
	const uint16_t imgHeight3 = 500;
	JiMP2::BMP bmp3(imgWidth3, imgHeight3);
	bmp3.setBackground();
	unsigned char color3[3]={255,255,255};
	//Light light(Vector(250,0,300),1,color3[0],color3[1],color3[2]);
	Light light(Vector(500,250,0),0.5,255,0,0);
	Light light2(Vector(0,250,0),0.5,0,255,255);
	ObjReader o;
	o.ReadVectors("deer.obj",250,400,0,0.25,255,255,0);
	long long size = o.getSize();
	for(uint16_t y=0; y<imgHeight3; y++){
		for(uint16_t x=0; x<imgWidth3; x++){
			//zamienic dir z orig ? 
			double t = 1000000;
			Ray ray(Vector(x,y,0), Vector(0,0,1)); 
			long long i=0;
			//cout<<t<<" t"<<endl;
			while(i<size){

				if(o.getT(i).cross(ray,t)){
				Vector pc = ray.getOrigin() + ray.getDirection()*t;

				Vector L = Normalize(light.getPos() -pc);
				Vector N = Normalize(o.getT(i).getNormal());

				//double dt = L.scalar(N);
				Vector L2 = Normalize(light2.getPos() -pc);
				Vector N2 = Normalize(o.getT(i).getNormal());

				double dt = L.scalar(N);
				double dt2 = L2.scalar(N2);
				double r,g,b;
				r=o.getT(i).getR()*0.5+ light.getR()*dt*light.getIntensity()*0.5+ light2.getR()*dt2*light2.getIntensity()*0.5;
				g=o.getT(i).getG()*0.5+ light.getG()*dt*light.getIntensity()*0.5+ light2.getG()*dt2*light2.getIntensity()*0.5;
				b=o.getT(i).getB()*0.5+light.getB()*dt*light.getIntensity()*0.5+ light2.getB()*dt2*light2.getIntensity()*0.5;
				if(r<0)r=0;
				if(g<0)g=0;
				if(b<0)b=0;
				if(r>255)r=255;
				if(g>255)g=255;
				if(b>255)b=255;
				bmp3.setPixel(x,y, (int)r,(int)g,(int)b);
				};
				i++;
			}
			cout<<x<<" "<<y<<endl;
		
			
		}
	}
	
	std::ofstream outfile("main7.bmp", std::ofstream::binary);
	outfile << bmp3;

	std::cout << "end." << std::endl;

return 0;
}