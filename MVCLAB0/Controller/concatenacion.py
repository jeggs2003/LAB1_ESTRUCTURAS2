class concatenacion:
    def process_companies(self, dpi, companies):
        result = []
        for company in companies:
            result.append(f"{company} - {dpi}")
        return result
