class MyHashSet {
private:
    vector<bool> numbers = vector<bool>(1000001, false);
public:
    MyHashSet(){
    }
    
    void add(int key) {
        this->numbers[key] = true;
    }
    
    void remove(int key) {
        this->numbers[key] = false;
    }
    
    bool contains(int key) {
        return this->numbers[key];
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */