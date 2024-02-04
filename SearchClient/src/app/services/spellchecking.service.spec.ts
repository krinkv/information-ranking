import { TestBed } from '@angular/core/testing';

import { SpellcheckingService } from './spellchecking.service';

describe('SpellcheckingService', () => {
  let service: SpellcheckingService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SpellcheckingService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
