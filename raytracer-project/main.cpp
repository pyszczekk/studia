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
#include <thread>
#include <vector>
#include "trace.h"
void foo(){std::cout<<"hello \n";};

int main(){
	std::thread e(foo);
	e.join();
	const uint16_t imgWidth = 500;
	const uint16_t imgHeight = 500;
	JiMP2::BMP bmp(imgWidth, imgHeight);
	bmp.setBackground(); 
	Sphere sphere(Vector(250, 250, 80), 80, 255,255,255,true);
	Sphere sphereb(Vector(350, 130, -80),90, 0,0,0,false);
	Sphere sphere2(Vector(150, 280, 0), 50, 255,0,255,true);
	Sphere sphere3(Vector(350, 280, 30), 40, 0,255,255,false);
	vector <Obj*> obj;//={new Sphere(Vector(250,130,0),80)};
	obj.push_back(&sphere);
	obj.push_back(&sphere2);
	obj.push_back(&sphere3);
	obj.push_back(&sphereb);
	unsigned char color[3]={255,255,255};
	Light light(Vector(0,250,0),1,255,255,255);
	Light light2(Vector(500,250,0),1,255,0,255);

	vector <Light> lights;
	lights.push_back(light);
	lights.push_back(light2);
	
	for(uint16_t y=0; y<imgHeight; y++){
		for(uint16_t x=0; x<imgWidth; x++){
			Ray ray(Vector(x,y,0), Vector(0,0,1));
			double t = 1000000;
			long long i=0;
			Obj *hitObject = NULL;
			//for(uint16_t i=0; i<4;++i){
				//cout<<trace(ray,obj,t,hitObject)<<endl;
				if(trace(ray,obj,t,hitObject,4)){
				Vector pc = ray.getOrigin() + ray.getDirection()*t;

				vector<Vector> L;
				Vector N = Normalize(hitObject->getNormal(pc));

				vector <double> dt;
				double r,g,b;
				for(vector<Light>::iterator it=lights.begin();it!=lights.end();++it){
					L.push_back(Normalize(it->getPos() -pc));
					dt.push_back((Normalize(it->getPos() -pc)).scalar(N));
				}
				double ref = 0.4;//obj[i]->getRef();
				//cout<<typeid(obj[i]);
				long long asd=0;
				double red=0;
				double green=0;
				double blue=0;
				if(hitObject->Phong()){
					//tutaj iterowanie po swietle i dodaanie lighta; albo w funkcji jakiejs C:
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

			//}
			}
		}
	}
	
	std::ofstream outfile("main.bmp", std::ofstream::binary);
	outfile << bmp;

	std::cout << "end." << std::endl;
return 0; 

}