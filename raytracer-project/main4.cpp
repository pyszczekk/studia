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
int main(){
	const uint16_t imgWidth3 = 500;
	const uint16_t imgHeight3 = 500;
	JiMP2::BMP bmp3(imgWidth3, imgHeight3);
	bmp3.setBackground();
	unsigned char color3[3]={255,255,255};
	Light light(Vector(500,500,500),1,color3[0],color3[1],color3[2]);
	ObjReader o;
	o.ReadVectors("cat.obj",300,320,0,0.5);
	long long size = o.getSize();
	for(uint16_t y=0; y<imgHeight3; y++){
		for(uint16_t x=0; x<imgWidth3; x++){
			Ray ray(Vector(x,y,0), Vector(0,0,1)); //zamienic dir z orig ? 
			double t = 1000000;
			long long i=0;
			
			while(i<size){

				if(o.getT(i).cross(ray,t)){
				Vector pc = ray.getOrigin() + ray.getDirection()*t;

				Vector L = Normalize(light.getPos() -pc);
				Vector N = Normalize(o.getT(i).getNormal());

				double dt = L.scalar(N);
				double r,g,b;
				r=255+ light.getR()*dt*light.getIntensity();
				g=255+ light.getG()*dt*light.getIntensity();
				b=0+light.getB()*dt*light.getIntensity();
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
	
	std::ofstream outfile("main4.bmp", std::ofstream::binary);
	outfile << bmp3;

	std::cout << "end." << std::endl;

return 0;
}