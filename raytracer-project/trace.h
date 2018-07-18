#ifndef _TRACE_H
#define _TRACE_H
bool trace( 
    Ray& ray, 
    vector<Obj*>obj, 
    double &tNear, Obj *&hitObject, int n=0) 
{ 
    tNear = 1000000000; 
    int i=0;
    n=obj.size();
   for(int i=0;i<n;++i){
   	double t=100000000;
   	if(obj.at(i)->cross(ray,t) && t<tNear){
   		  hitObject = obj.at(i);
   		  tNear=t;
   	}
   }
 
   return !(hitObject == NULL); 
}
#endif