#ifndef _TRIANGLE_H
#define _TRIANGLE_H
#include<iostream>
#include <math.h>
#include "vec.h"
#include "ray.h"
#include "obj.h"
class Triangle:public Obj{
private:
	Vector a,b,c;
	unsigned char rc=120;
	unsigned char gc=120;
	unsigned char bc=120;


public:
	Triangle(){};
	Triangle(Vector _a, Vector _b, Vector _c):a(Vector(_a.getX(),_a.getY(),_a.getZ())),b(Vector(_b.getX(), _b.getY(),_b.getZ())),c(Vector(_c.getX(),_c.getY(),_c.getZ())){};
	
	Triangle(Vector _a, Vector _b, Vector _c, unsigned char r, unsigned char g, unsigned char _bc):a(Vector(_a.getX(),_a.getY(),_a.getZ())),b(Vector(_b.getX(), _b.getY(),_b.getZ())),c(Vector(_c.getX(),_c.getY(),_c.getZ())), rc(r),gc(g),bc(_bc){};
	 Triangle(const Triangle& t){a=t.a;b=t.b;c=t.c; rc=t.rc; gc=t.gc; bc=t.bc;};
	~Triangle(){};
	bool cross(Ray& ray, double& t){
		Vector o = ray.getOrigin();
		Vector r = ray.getDirection();
		//moller-trumbore algorithm
		Vector ab = b-a;
		Vector ac = c-a;
		Vector pvec = r*ac;
		Vector N = Normalize(ab*ac);
		if (r.scalar(N) >= 0)return false;//dwustronnosc;
		double det = ab.scalar(pvec);
		if(fabs(det)<0.000001) return false;
		double invdet = 1/det;
		Vector tvec = o-a;
		double u,v;
		 u = tvec.scalar(pvec) * invdet; 
    	if (u < 0 || u > 1) return false; 
    	Vector qvec =tvec*ab;
    	v = r.scalar(qvec) * invdet; 
    	if (v < 0 || u + v > 1) return false;
    	 t = ac.scalar(qvec) * invdet; 

    	 if(t>0)return true;
    	 else return false;
    	
	};
	Vector getNormal(){
		Vector ab = b-a;
		Vector ac = c-a;
		Vector p = ab*ac;
		double s =sqrt(p.getX()*p.getX()+p.getY()*p.getY()+p.getZ()*p.getZ());
		return (p/s);
	}
	void set_values(Vector _a, Vector _b, Vector _c){
		a=_a;
		b=_b;
		c=_c;

	}
	void set_color(unsigned char r, unsigned char g, unsigned char _b){
		rc=r;
		gc=g;
		bc=_b;
	}
	bool Phong(){return false;}
	unsigned char getR(){return rc;}
	unsigned char getG(){return gc;}
	unsigned char getB(){return bc;}

};
#endif