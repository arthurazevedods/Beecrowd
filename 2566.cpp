#include <iostream>
#include <list>
#include <queue>
#define MAX 100000

using namespace std;

class Graph{
private:
	int node;
	list<pair<int, int> > * adj;

public:
	Graph(int node){
		this->node = node;
		adj = new list<pair<int, int> >[node];
	}

	void addEdge(int v1, int v2, int real){
		adj[v1].push_back(make_pair(v2, real));
	}

	
	int dijkstra(int started, int dest){
		int dist[node];

		int visited[node];

		
		priority_queue < pair<int, int>,vector<pair<int, int> >, greater<pair<int, int> > > priority;

		for(int i = 0; i < node; i++){
			dist[i] = MAX;
			visited[i] = false;
		}

		dist[started] = 0;
		priority.push(make_pair(dist[started], started));

		while(!priority.empty()){
			pair<int, int> p = priority.top();
			int current = p.second;
			priority.pop();

			if(visited[current] == false){

				visited[current] = true;
				list<pair<int, int> >::iterator it;

				for(it = adj[current].begin(); it != adj[current].end(); it++){
					int N = it->first;
					int price = it->second;

					if(dist[N] > (dist[current] + price)){
						dist[N] = dist[current] + price;
						priority.push(make_pair(dist[N], N));
					}
				}
			}
		}
		return dist[dest];
	}
};

int main(){
	

	int N,M,A,B,T,R,distBus,distAir; 

	while(scanf("%d %d",&N,&M)!=EOF){
		Graph Bus(MAX);
		Graph Air(MAX);
		for(int i = 1;i <= M;i++){
			scanf("%d %d %d %d",&A,&B,&T,&R);

			if(T==0){
				Bus.addEdge(A,B,R);
			}else{
				Air.addEdge(A,B,R);
			}

		}

		distBus = Bus.dijkstra(1,N); 
		distAir = Air.dijkstra(1,N);

		if(distBus < distAir){
			cout << distBus << endl;
		}else{
			cout << distAir << endl;
		}
	}


	return 0;
}