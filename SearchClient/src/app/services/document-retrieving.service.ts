import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class DocumentRetrievingService {

  constructor() { }

  getBestDocumentCandidates(query: String) {
    return null;
  }
}
