class Vector:
    def __init__(self,vec):
        self.vec=vec

    def __str__(self):
        str1=""
        index=0
        for i in self.vec:
            str1+=f" {i}a{index} +"
            index+=1
        return str1[:-1]
    
    def __len__(self):
        return len(self.vec)

    def __add__(self,vec2):
        self.vec2=vec2
        if len(self.vec)==len(self.vec2):
            newlist=[]
            for i in range(len(self.vec)):
                newlist.append(self.vec[i] + vec2.vec[i])
            return Vector(newlist)
        else:
            return f"Addition failled the length of these two vectors is not same"

    def __mul__(self,vec2):
        self.vec2=vec2
        if len(self.vec)==len(self.vec2):
            sum=0
            for i in range(len(self.vec)):
                sum+=(self.vec[i]*vec2.vec[i])
            return sum
        else:
            return f"Multiplication failled the length of these two vectors is not same"

v1=Vector([1,4,6,4])
v2=Vector([1,6,9])
print(v1+v2)
print(v1*v2)
print(f"Dimension of vector v1 is : {len(v1)}")
print(f"Dimension of vector v2 is : {len(v2)}")
