#include <iostream>
#include <list>
#include <queue>
#define MAX 100000

using namespace std;

class Graph{
public:
	int node;
	list<pair<int, int>> * edge;

	Graph(int node){
		this->node = node;
		edge = new list<pair<int, int> >[node];
	}

	void addEdge(int from_node, int to_node, int price){
		edge[from_node].push_back(make_pair(to_node, price));
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

				for(it = edge[current].begin(); it != edge[current].end(); it++){
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
	int cidades, estradas ;
	scanf("%d %d",&cidades,&estradas);

	Graph graph(cidades);
	Graph graph2(cidades);

	for(int i = 0; i < estradas; i++){
		int A, B, price;
		scanf("%d %d %d",&A,&B,&price);

		graph.addEdge(A-1,B-1,price);
		graph.addEdge(B-1,A-1,price);
	}

	for(int i = 0; i < cidades; i++){
		list<pair<int, int> >::iterator it;
		for(it = graph.edge[i].begin(); it != graph.edge[i].end(); it++){
			int edge = it->first;
			int price = it->second;
			list<pair<int, int> >::iterator it2;
			bool len_edge = graph.edge[edge].size();
			if(len_edge == 1){
				for(it2 = graph.edge[edge].begin(); it2 != graph.edge[edge].end(); it2++){
					int edge2 = it2->first;
					int price2 = it2->second;
					graph2.addEdge(i, edge2, price + price2);
				}
			}
		}
	}
	
	int min_par = graph2.dijkstra(0, cidades-1);
	
	if(min_par == MAX){
		cout << "-1" << endl;
	}
	else{
		cout << min_par << endl;
	}

	return 0;
}