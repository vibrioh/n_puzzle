import sys
import copy
import queue
import time
import resource
import itertools
import math


class Node:
    def __init__(self, state, backward = None, parent = None):
        self.state = state
        self.backward = backward
        self.parent = parent
        if parent:
            depth = parent.depth + 1
        else:
            depth = 0
        self.depth = depth

class Solver:
    def __init__(self, board):
        self.board = board
        self.input_n = len(self.board)
        self.grid_n = int(math.sqrt(self.input_n))
        
        self.node = Node(board)
        self.state = self.node.state
        self.goal = list(range(len(board)))

    def grid_by_key(self, state, key):
        row = int(state.index(key) / self.grid_n)
        col = state.index(key) % self.grid_n
        return row, col

    def manhattan_d(self, node):
        distance = 0
        i = 0
        while i < self.input_n - 1 :
            i += 1
            row, col = self.grid_by_key(node.state, i)
            r_goal, c_goal = self.grid_by_key(self.goal, i)
            distance += abs(row - r_goal) + abs(col - c_goal)
        return distance

    # def misplace_t(self, node):
    #     tile = 0
    #     i = 0
    #     while i < self.input_n - 1:
    #         i += 1
    #         row, col = self.grid_by_key(node.state, i)
    #         r_goal, c_goal = self.grid_by_key(self.goal, i)
    #         if row != r_goal or col != c_goal:
    #             tile += 1
    #     return tile


    def hueristic(self,node):
        h1 = self.manhattan_d(node)
        # h2 = self.misplace_t(node)
        # h = h1 + h2
        g = node.depth
        score = g + h1
        return score


    def grid_0(self, state):
        return self.grid_by_key(state, 0)

    def g_up(self, state):
        row, col = self.grid_0(state)
        return row - 1, col

    def g_down(self, state):
        row, col = self.grid_0(state)
        return row + 1, col

    def g_left(self, state):
        row, col = self.grid_0(state)
        return row, col - 1

    def g_right(self, state):
        row, col = self.grid_0(state)
        return row, col + 1

    def idx(self, grid):
        row, col = grid
        return row * self.grid_n + col

    def state_child(self, state, idx_k):
        child = copy.deepcopy(state)
        idx_0 = state.index(0)
        child[idx_0] = state[idx_k]
        child[idx_k] = 0
        return child

    def nodes_expand(self, node):
        self.expand += 1
        children = []
        direction = ['up', 'down', 'left', 'right']
        if node.backward:
            direction.remove(node.backward)
        state = node.state
        row, col = self.grid_0(state)
        for i in direction:
            if i == 'up' and row > 0:
                up_idx = self.idx(self.g_up(state))
                up_state = self.state_child(state, up_idx)
                up_node = Node(up_state, backward = 'down', parent = node)
                children .append(up_node)
            if i == 'down' and row < math.sqrt(self.input_n) - 1:
                down_idx = self.idx(self.g_down(state))
                down_state = self.state_child(state, down_idx)
                down_node = Node(down_state, backward = 'up', parent = node)
                children .append(down_node)
            if i == 'left' and col > 0:
                left_idx = self.idx(self.g_left(state))
                left_state = self.state_child(state, left_idx)
                left_node = Node(left_state, backward = 'right', parent = node)
                children .append(left_node)
            if i == 'right' and col < math.sqrt(self.input_n) - 1:
                right_idx = self.idx(self.g_right(state))
                right_state = self.state_child(state, right_idx)
                right_node = Node(right_state,  backward = 'left', parent = node)
                children .append(right_node)
        return children 

    def is_goal(self, state):
        return state == self.goal

    def bfs(self):
        frontier = queue.Queue()
        explored = set()
        self.expand = 0
        self.fringe_set = set()
        self.depth_set = set()
        frontier.put(self.node)
        explored.add(str(self.node.state))
        while frontier.empty() != True:
            node_new = frontier.get()
            if self.is_goal(node_new.state):
                self.fringe = frontier.qsize()
                return self.solution(node_new)
            children_list = self.nodes_expand(node_new)
            while children_list:
                candidate = children_list.pop(0)
                depth = candidate.depth
                self.depth_set.add(depth)
                if str(candidate.state) not in explored:
                    frontier.put(candidate)
                    explored.add(str(candidate.state))
                    self.fringe_set.add(frontier.qsize())
        print('no solution')

    def dfs(self):
        frontier = queue.LifoQueue()
        explored = set()
        self.expand = 0
        self.fringe_set = set()
        self.depth_set = set()
        frontier.put(self.node)
        explored.add(str(self.node.state))
        while frontier.empty() != True:
            node_new = frontier.get()
            if self.is_goal(node_new.state):
                self.fringe = frontier.qsize()
                return self.solution(node_new)
            children_list = self.nodes_expand(node_new)
            while children_list:
                candidate = children_list.pop()
                depth = node_new.depth
                self.depth_set.add(depth)
                if str(candidate.state) not in explored:
                    frontier.put(candidate)
                    explored.add(str(candidate.state))
                    self.fringe_set.add(frontier.qsize())
        print('no solution')

    def ast(self):
        frontier = queue.PriorityQueue()
        explored = set()
        self.expand = 0
        self.fringe_set = set()
        self.depth_set = set()
        seq = itertools.count()
        frontier.put((self.hueristic(self.node), next(seq), self.node))
        explored.add(str(self.node.state))
        while frontier.empty() != True:
            node_new = frontier.get()[2]
            if self.is_goal(node_new.state):
                self.fringe = frontier.qsize()
                return self.solution(node_new)
            children_list = self.nodes_expand(node_new)
            while children_list:
                candidate = children_list.pop(0)
                depth = candidate.depth
                self.depth_set.add(depth)
                if str(candidate.state) not in explored:
                    frontier.put((self.hueristic(candidate), next(seq), candidate))
                    explored.add(str(candidate.state))
                    self.fringe_set.add(frontier.qsize())
        print('no solution')

    def ida(self):
        new_limit = 0
        node_back = None
        while node_back == None:
            node_new, new_limit = self._ida(new_limit)
            node_back = node_new
            new_limit += 1

    def _ida(self, limit):
        frontier = queue.LifoQueue()
        explored = {}
        self.expand = 0
        self.fringe_set = set()
        self.depth_set = set()
        frontier.put(self.node)
        explored[str(self.node.state)] = self.hueristic(self.node)
        new_limit = limit
        while frontier.empty() != True:
            node_new = frontier.get()
            if self.is_goal(node_new.state):

                self.fringe = frontier.qsize()
                self.solution(node_new)
                return node_new, new_limit
            else:
                children_list = self.nodes_expand(node_new)
                for candidate in children_list:
                    explored[str(candidate.state)] = self.hueristic(candidate)
                    self.depth_set.add(candidate.depth)
                    if self.hueristic(candidate) < new_limit:
                        if str(candidate.state) not in explored or explored[str(candidate.state)] < new_limit:
                            frontier.put(candidate)
                            self.fringe_set.add(frontier.qsize())


        return None, new_limit

    def solution(self, node):
        node_g = node
        forward = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}
        path_to_goal = []
        while node_g.state != self.board :
            move = forward[node_g.backward]
            path_to_goal.append(move)
            node_g =  node_g.parent
        path_to_goal.reverse()
        print('path_to_goal:', path_to_goal)
        print('cost_of_path:', len(path_to_goal))
        print('nodes_expanded:', self.expand)
        print('fringe_size:', self.fringe)
        print('max_fringe_size:', max(self.fringe_set))
        print('search_depth:', node.depth)
        print('max_search_depth:',  max(self.depth_set))


def main():
    start_time = time.clock()
    start_ram = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    func = getattr(Solver([int(x) for x in sys.argv[2].split(',')]), sys.argv[1])
    func()
    end_ram = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    end_time = time.clock()
    print('running_time:', "%.8f" % (end_time - start_time))
    print('max_ram_usage:', "%.8f" % ((end_ram - start_ram) / (1024*1024)))

if __name__ == '__main__':
    file = open('output.txt', 'w')
    sys.stdout = file
    main()
    file.close()



