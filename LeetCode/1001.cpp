#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <array>
using namespace std;

class Solution
{
public:
	vector<int> gridIllumination(int N, vector<vector<int>>& lamps, vector<vector<int>>& queries)
	{
		mN = N;
		for (const auto& a : lamps)
		{
			long long x = a[0];
			long long y = a[1];
			mLamps.emplace(x + y * 1000000001);
			++mLines[0][x];
			++mLines[1][y];
			++mLines[2][x - y];
			++mLines[3][x + y];
		}
		for (const auto& q : queries)
		{
			long long x = q[0];
			long long y = q[1];
			if (mLines[0].find(x) == mLines[0].end() and
				mLines[1].find(y) == mLines[1].end() and
				mLines[2].find(x - y) == mLines[2].end() and
				mLines[3].find(x + y) == mLines[3].end())
			{
				mAns.emplace_back(0);
			}
			else
			{
				mAns.emplace_back(1);
			}
			Remove(x, y);
			Remove(x - 1, y);
			Remove(x, y - 1);
			Remove(x + 1, y);
			Remove(x, y + 1);
			Remove(x - 1, y - 1);
			Remove(x + 1, y + 1);
			Remove(x - 1, y + 1);
			Remove(x + 1, y - 1);
		}
		return mAns;
	}
private:
	long long mN;
	unordered_set<unsigned long long> mLamps;
	// x, y, x-y, x+y
	array<unordered_map<long long, size_t>, 4> mLines;
	vector<int> mAns;

	void Remove(long long x, long long y)
	{
		if (0 <= x and x < mN and 0 <= y and y < mN)
		{
			const auto& f = mLamps.find(x + y * 1000000001);
			if (f != mLamps.end())
			{
				if (--mLines[0][x] == 0) mLines[0].erase(x);
				if (--mLines[1][y] == 0) mLines[1].erase(y);
				if (--mLines[2][x - y] == 0) mLines[2].erase(x - y);
				if (--mLines[3][x + y] == 0) mLines[3].erase(x + y);
				mLamps.erase(f);
			}
		}
	}

};

int main()
{
	Solution s;
	vector<vector<int>> l;
	l.emplace_back(vector<int>({ 0,0 }));
	l.emplace_back(vector<int>({ 4,4 }));
	vector<vector<int>> q;
	q.emplace_back(vector<int>({ 1,1 }));
	q.emplace_back(vector<int>({ 1,0 }));
	auto g = s.gridIllumination(5, l, q);
	return 0;
}