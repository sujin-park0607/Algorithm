#include <iostream>
#include <unordered_map>
#include <set> 
#include <algorithm>
#include <stdio.h>
struct Student {
    int grade;
    int gender;     //0 남자, 1 여자
    int score;
 
    void init(int _grade, int _gender, int _score) {
        grade = _grade;
        gender = _gender;
        score = _score;
    }
};

typedef pair<int, int> pii;
unordered_map<int, Student > map;     // key = id, value = student
set<pii> priority[4][2];              // [grade][gender] = {score, id}
 
 
void init() {
    map.clear();
    for (register int i = 0; i < 4; i++) {
        for (register int j = 0; j < 2; j++)
            priority[i][j].clear();
    }
}
 
int add(int mId, int mGrade, char mGender[7], int mScore) {
    int a = mGender[0] == 'm' ? 0 : 1;
    map[mId] = { mGrade, a, mScore };
    priority[mGrade][a].insert({ mScore, mId });
 
    return priority[mGrade][a].rbegin()->second;
}
 
int remove(int mId) {
    if (map.count(mId) == 0)
        return 0;
 
    Student tmp = map[mId];
    auto it = priority[tmp.grade][tmp.gender].find({ tmp.score, mId });
    priority[tmp.grade][tmp.gender].erase(it);
    map.erase(mId);
    return priority[tmp.grade][tmp.gender].empty() ? 0 : priority[tmp.grade][tmp.gender].begin()->second;
}
 
int query(int mGradeCnt, int mGrade[], int mGenderCnt, char mGender[][7], int mScore) {
    pii ret = { 300001,0 };
    for (register int i = 0; i < mGradeCnt; i++) {
        for (register int j = 0; j < mGenderCnt; j++) {
            int grade = mGrade[i];
            int gender = mGender[j][0] == 'm' ? 0 : 1;
 
            auto it = priority[grade][gender].lower_bound({ mScore,0 });
            if (it != priority[grade][gender].end()) {
                ret = min(ret, *it);
            }
        }
    }
    return ret.second;
}