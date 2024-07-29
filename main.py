import pickle
import argparse
from planner import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Write the ids of the starting point and ending point.")
    parser.add_argument("-f" , "--frm", required=True, help="start node")
    parser.add_argument("-t", "--to", required=True, help="end node")
    parser.add_argument("-w", "--weight", required=True, nargs="+", help="alpha, beta, gamma")
    parser.add_argument("-s", "--save", required=True, help="save or not")

    args = parser.parse_args()

    frm = int(args.frm)
    to = int(args.to)
    alpha, beta, gamma = args.weight
    alpha, beta, gamma = int(alpha), int(beta), int(gamma)
    save = args.save
    save = int(save)

    planner = RoutingPlanner(alpha, beta, gamma)
    if save:
        planner.astar_path(frm, to)
        print("save in ./result/optimal_path.csv")
    else:
        print(planner.astar(frm, to))
