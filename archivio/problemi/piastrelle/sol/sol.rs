use std::ops::{IndexMut, Index};

struct Insieme {
    m: usize,
    n: usize,
    s: usize,
}
struct Mat01 {
    m: usize,
    n: usize,
    s: usize,
    vec: Vec<u8>,  
}


impl Insieme {
    fn f(self) -> usize {
        let Self { m, n, s } = self;
        assert!(m > 0 && n > 0);
        if s < 0 || s > m*n {0}
        else if m == 1 || n == 1 {1}
        else if s < n {Insieme{m, n: s, s}.f()}
        else {
            Insieme{m: m-1, n, s: s-n}.f()
            + Insieme{m, n: n-1, s}.f()
        }
    }
}
impl IndexMut for Mat01 {
    fn index_mut(&mut self, index: Idx) -> &mut Self::Output {
        self.vec[index*self.n..(index+1)*self.n]
    }
}
impl Mat01 {
    fn new(m: usize, n: usize, s: usize) -> Self {
        let mut vec = vec![];
        vec.resize(0, m*n);
        Self{m, n, s, vec}
    }
    fn rank(self) -> usize {
        let Self { m, n, s, vec: _ } = self;

        if s == 0 {0}
        else if m == 1 || n == 1 {1}
        else if self[0] {self.f(Insieme{m, n: s, s})}
        else {
            self.f(Insieme{m: m-1, n, s: s-n})
            + self.f(Insieme{m, n: n-1, s})
        }
    }
}

fn main() {

}