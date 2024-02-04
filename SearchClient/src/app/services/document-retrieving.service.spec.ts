import { TestBed } from '@angular/core/testing';

import { DocumentRetrievingService } from './document-retrieving.service';

describe('DocumentRetrievingService', () => {
  let service: DocumentRetrievingService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DocumentRetrievingService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
