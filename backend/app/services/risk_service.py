class RiskService:

    def __init__(self, graph):

        self.graph = graph

    def total_risk(self, path):

        total = 0

        for i in range(len(path) - 1):

            source = path[i]
            destination = path[i + 1]

            road = self.graph.neighbors(source)[destination]

            total += road["risk"]

        return round(total, 2)

    def average_risk(self, path):

        if len(path) < 2:
            return 0

        total = self.total_risk(path)

        average = total / (len(path) - 1)

        return round(average, 2)

    def safety_percentage(self, path):

        avg = self.average_risk(path)

        safety = (1 - avg) * 100

        if safety < 0:
            safety = 0

        return round(safety, 2)

    def risk_status(self, path):

        avg = self.average_risk(path)

        if avg < 0.30:
            return "SAFE"

        elif avg < 0.60:
            return "MODERATE"

        else:
            return "DANGEROUS"