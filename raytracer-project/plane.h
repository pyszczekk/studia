#ifndef _PLANE_H
#define _PLANE_H
#include "vec.h"
#include "tiangle.h"
class Plane:public Obj{
	private:
		Vector a,b,c,d;
		Triangle abc, bcd;
	public:
		Plane(Vector _a, Vector _b, Vector _c, Vector _d):a(_a),b(_b),c(_c),d(_d){
			abc=Triangle(_a,_b,_c);
			bcd=Triangle(_b, _c, _d);
		};
		Plane(const Plane& p){
			a=p.a;
			b=p.b;
			c=p.c;
			d=p.d;
			abc=Triangle(a,b,c);
			bcd=Triangle(b,c,d);
		}

};
#endif