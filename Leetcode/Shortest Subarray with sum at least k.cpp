#include<iostream>
#include<queue>
#include<algorithm>
#include<vector>
#include<functional>
using namespace std;
class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        int n=nums.size();
        vector<long long> prefix(n+1,0);
        for(int i=1;i<=n;i++){
           prefix[i] = prefix[i-1] + nums[i-1];
        }
        deque<int> dq;
        int minLen = n+1;
        for(int i=0;i<=n;i++){
            while(!dq.empty() && prefix[i]-prefix[dq.front()] >= k){
                minLen = min(minLen,i-dq.front());
                dq.pop_front();
                }
            while(!dq.empty() && prefix[i]<=prefix[dq.back()]){
                dq.pop_back();

            }
            dq.push_back(i);
        }
        return minLen <= n ? minLen : -1;
    }
};