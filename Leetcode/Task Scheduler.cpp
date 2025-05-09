#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> count;
        int max_count = 0;

        // Count frequency of each task
        for (const auto& task : tasks) {
            count[task]++;
            max_count = max(max_count, count[task]);
        }

        // Count number of tasks that have max frequency
        int num_max = 0;
        for (const auto& kvp : count) {
            if (kvp.second == max_count) {
                num_max++;
            }
        }

        // Calculate the minimum required intervals
        int part_count = max_count - 1;
        int part_length = n - (num_max - 1);
        int empty_slots = part_count * part_length;
        int available_tasks = tasks.size() - max_count * num_max;
        int idles = max(0, empty_slots - available_tasks);

        return tasks.size() + idles;
    }
};
