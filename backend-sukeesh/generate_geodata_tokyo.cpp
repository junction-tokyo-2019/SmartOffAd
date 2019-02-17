#include <iostream>
#include <map>

using namespace std;

#define ld double

ld left_lat = 35.666125;
ld left_lon = 139.622401;

ld top_lat = 35.821190;
ld top_lon = 139.772807;

ld right_lat = 35.723466;
ld right_lon = 139.913261;

ld bottom_lat = 35.518437;
ld bottom_lon = 139.708876;

ld mid_lat = 35.6698135;
ld mid_lon = 139.767831;

ld lat_degree_for_two_km = 0.0018018;
ld lon_degree_for_two_km = 0.0022094;   
// approx ~ cosine(lat) * length of degree (miles) at equator

map <pair<ld, ld>, bool> isVisited;

bool isNotOK(ld lat, ld lon){
	if (lat < left_lat || lat > right_lat || lon > top_lon || lon < bottom_lon) {
		return false;
	}
	return true;
}

void dfs(ld lat, ld lon){
	if (!isNotOK(lat, lon)) {
		return;
	}
	if (isVisited[make_pair(lat, lon)] == 1) {
		return;
	}
	isVisited[make_pair(lat, lon)] = 1;
	printf("%.6f %.6f\n", lat, lon);

	dfs(lat - lat_degree_for_two_km, lon);
	dfs(lat + lat_degree_for_two_km, lon);
	dfs(lat, lon - lon_degree_for_two_km);
	dfs(lat, lon + lon_degree_for_two_km);

	// get from corners
	dfs(lat + lat_degree_for_two_km, lon + lon_degree_for_two_km);
	dfs(lat - lat_degree_for_two_km, lon - lon_degree_for_two_km);
	dfs(lat + lat_degree_for_two_km, lon - lon_degree_for_two_km);
	dfs(lat - lat_degree_for_two_km, lon + lon_degree_for_two_km);
}

void generate_geodate(){
	dfs(mid_lat, mid_lon);
}

int main(){
	generate_geodate();

	return 0;
}
