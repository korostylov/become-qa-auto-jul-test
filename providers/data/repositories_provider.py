class RepositoriesProvider:
    
    @staticmethod
    def existing_repository():
        return {
            'name': 'become-qa-auto-test',
            'total_count': 1,
            'items_count': 1
        }
    
    @staticmethod
    def non_existing_repository():
        return {
            'name': 'become-qa-auto-test-12344',
            'total_count': 0,
            'items_count': 0
        }
